# insta_story_upload

Tech stack- Flask framework, MySql db, ORM(sqlAlchemy)

Api:
1. http://127.0.0.1:65531/story/upload_file
It takes all the input for story upload and internally call the API:
http://127.0.0.1:65531/story/upload_image which has all the validation on image upload

2. http://127.0.0.1:65531/story/get_recent_stories
It retrives all the story added and sort them with the recent time stamp.
