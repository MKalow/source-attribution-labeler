import os

from pandas import DataFrame, read_csv, Series
from praw.models import Submission
from prawcore import TooManyRequests, ServerError

from client import ScraperClient
from logger import set_tracker_logger
from settings import *
from utils import retry, set_and_get_wd, convert_timestamp

tracker_logger = set_tracker_logger()


def run():
    df, file_path, columns = _load_or_create_df()
    client = ScraperClient()
    try:
        submissions = client.get_submissions()
    except Exception as exp:
        print(f'got exp {exp}')
        submissions = []

    # see here what a submission contains:
    # https://praw.readthedocs.io/en/stable/code_overview/models/submission.html
    for _, submission in enumerate(submissions):
        try:
            row = [
                str(submission.id),
                str(submission.name),
                str(submission.url),
                _get_author_name(submission),
                _get_post_creation_time(submission),
                _get_was_post_edited(submission),
                str(submission.distinguished),
                str(submission.is_original_content),
                str(submission.locked),
                str(submission.stickied),
                str(submission.over_18),
                str(submission.title),
                _get_post_content(submission),
                str(submission.num_comments),
                _get_top_level_comments_count(submission),
                str(submission.score),
                str(submission.upvote_ratio),
                *_get_top_comments_info(submission)
            ]
        except Exception as exp:
            print(f'got exp {exp}; Skipping submission {submission.id}')
            continue

        df = _append_or_update_df(df, row, columns)

    df.to_csv(file_path, index=False)
    print(file_path)


def _load_or_create_df():
    columns = [
        'Submission id',
        'Submission Name',
        'Submission url',
        'Author',
        'Creation time',
        'Edited',
        'Distinguished',
        'Is original content',
        'Locked',
        'Stickied',
        'NSFW',
        'Title',
        'Content',
        'Number of total comments',
        'Number of top level comments',
        'Post Upvote',
        'Upvote ratio',
        *_generate_comments_columns()
    ]
    file_path = os.path.join(set_and_get_wd(), f'{EXPORT_FILE_NAME}.csv')
    if os.path.isfile(file_path):
        df = read_csv(file_path, index_col=False)
    else:
        df = DataFrame(columns=columns)
    return df, file_path, columns


def _generate_comments_columns():
    return [f'Comment {i + 1}' for i in range(MAX_COMMENTS_DATA)] + \
           [f'Upvote {i + 1}' for i in range(MAX_COMMENTS_DATA)] + \
           [f'Creation time {i + 1}' for i in range(MAX_COMMENTS_DATA)]


def _get_author_name(post: Submission):
    try:
        return str(post.author.name)
    except Exception as exp:
        print(f'got exp {exp} on submission {post.id}')
        return ""


def _get_post_creation_time(post: Submission):
    return convert_timestamp(post.created_utc)


def _get_was_post_edited(post: Submission):
    edited = post.edited
    if isinstance(edited, bool):
        return str(edited)
    try:
        return convert_timestamp(edited)
    except (TypeError, ValueError, OSError):
        return str(edited)


def _get_post_content(post: Submission):
    # when a post is not 'self', this is referring to old posts in reddit,
    # that used to be a 'link' to other websites and not a submission.
    return post.selftext if post.is_self else post.url


@retry(times=3, exceptions=(TooManyRequests, ServerError))
def _get_top_level_comments_count(post: Submission):
    count = 0
    for _ in post.comments:
        count += 1
    return count


@retry(times=3, exceptions=(TooManyRequests, ServerError))
def _get_top_comments_info(post: Submission):
    # CommentForest object hold multiple top-level comments.
    # This function returns list of data about X top-level comments: ['content1',..,'contentX',score1,..,scoreX]

    comments_content = [''] * MAX_COMMENTS_DATA
    comments_score = [''] * MAX_COMMENTS_DATA
    comments_creation_time = [''] * MAX_COMMENTS_DATA
    try:
        for idx, comment in enumerate(post.comments[:MAX_COMMENTS_DATA]):
            # https://praw.readthedocs.io/en/stable/code_overview/models/comment.html#praw.models.Comment
            comments_content[idx] = comment.body
            comments_score[idx] = comment.score
            comments_creation_time[idx] = convert_timestamp(comment.created_utc)

    except Exception as exp:
        print(f'got exp {exp}')

    return comments_content + comments_score + comments_creation_time


def _append_or_update_df(df, row, columns):
    row_series = Series(row, index=columns)
    if row[0] in df['Submission id'].values:
        indices_to_update = df[df['Submission id'] == row[0]].index[0]
        df.loc[indices_to_update] = row_series
        print(f'update {row[0]}')
        tracker_logger.info('update', f'{row[0]}')
    else:
        df.loc[len(df)] = row_series
        print(f'append {row[0]}')
        tracker_logger.info('append', f'{row[0]}')
    return df


if __name__ == '__main__':
   