# PreSetup
***
## GitHub
1. Go to [github](https://www.github.com) and either sign in or create an account
2. Over toward the right of the page, click on **New Repository**
3. Give the repository(repo) a short meaningful name. In this instance I named the repo **698-final-project**.
4. You can add a description if you want but leave everything else the same, and hit **Create Repository**.

This will setup an empty github repo to use
***
##Docker Cloud
1. Go to [Docker Cloud](https://cloud.docker.com) and either sign in or crete an account
2. If you have already connected Docker cloud to Git Hub go to step 7
3. Click on your user name in the top right and select **Cloud Settings from the dropdown
4. Go to **Source Providers** and click on the little plug icon to the right of GitHub
5. Sign in to GitHub
6. Click on the docker cloud icon in the top left
7. At the bottom of the page select **Create Repository**
8. Give it th esame name as your GitHub repo
9. Select the GitHub icon below, and and select the organization, and repo you setup in GitHub
10. Under that click on **Click here to customize the build settings**
11. It should have one setup already for master making a latest tag... leave that one alone and select the + next to build rules.
12. Change the new rule to have the settings below
  - **Source Type:** Tag
  - **Source:** /^[0-9.]+$/
  - **Docker Tag:** release-{sourceref}
  - **Dockerfile location:** Dockerfile
  - **Build Caching:** on
  ![What it should look like... there should be an image here](markdown-stuff/docker-settings.png)
13. Lastly hit the **Create** button at the bottom
