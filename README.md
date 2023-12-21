# flask_deployement

# Task 1

Successfully deployed my project for the first time with the guidance from this [video](https://www.youtube.com/watch?v=pg11wmj8LbY). Check out the deployed [service](https://trying-to-deploy.onrender.com/) and the corresponding [GitHub repository](https://trying-to-deploy.onrender.com/).

## Procedure

1. Create a GitHub repository.

2. Open your preferred code editor.

3. Create a `requirements.txt` file, including Flask and Gunicorn.

4. Copy the code from this [link](https://www.geeksforgeeks.org/flask-creating-first-simple-application/).

5. Avoid pasting the following lines:

    ```python
    if __name__ == '__main__':
        app.run()
    ```

6. Push the changes to GitHub.

7. Connect the repository to Render.

8. Set the build command to:

    ```
    gunicorn app:app
    ```

