# How to Upload MIRA to GitHub

Since I have already prepared the project locally (initialized git and created the first commit), you just need to connect it to GitHub.

## Step 1: Create the Repository on GitHub
1.  Open your browser and go to: **[https://github.com/new](https://github.com/new)**
2.  **Repository name**: Enter `Mira` (or any name you like).
3.  **Description**: (Optional) e.g., "Advanced OSINT Chatbot with AI Detective Mode".
4.  **Public/Private**: Choose **Public** (anyone can see) or **Private** (only you).
5.  **Initialize this repository with**:
    *   [ ] Add a README file (**UNCHECK** this - we already have one)
    *   [ ] Add .gitignore (**UNCHECK** this - we already have one)
    *   [ ] Choose a license (**UNCHECK** this)
6.  Click **Create repository**.

## Step 2: Push the Code
Once created, you will see a page with setup commands. You need to run the commands under **"…or push an existing repository from the command line"**.

Copy and run these commands in your MIRA terminal one by one:

1.  **Rename the branch to main:**
    ```bash
    git branch -M main
    ```

2.  **Add your GitHub URL** (Replace `YOUR_USERNAME` with your actual GitHub username):
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/Mira.git
    ```

3.  **Push the code:**
    ```bash
    git push -u origin main
    ```

## Troubleshooting: "Password authentication is not supported"
If you see the error: `remote: Support for password authentication was removed...` or `Invalid username or token`, do this:

1.  **Do NOT use your GitHub password.**
2.  You must generate a **Personal Access Token (PAT)**:
    *   Go to **[GitHub Settings > Developer settings > Personal access tokens > Tokens (classic)](https://github.com/settings/tokens/new)**.
    *   Note/Name: "Mira Upload".
    *   Expiration: 30 days (or no expiration).
    *   **Scopes**: Check the box for **`repo`** (Full control of private repositories).
    *   Click **Generate token**.
3.  **Copy the token** (it starts with `ghp_...`).
4.  Run `git push -u origin main` again.
    *   **Username**: `yousefbassem95-lang`
    *   **Password**: [PASTE THE TOKEN HERE] (It won't show on screen).

## Success!
Refesh your GitHub repository page. You should see all your files (`mira.py`, `modules/`, `README.md`, etc.) listed there.
