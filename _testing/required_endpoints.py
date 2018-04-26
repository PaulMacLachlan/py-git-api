# for our API connection well need the following endpoints to pull/push keys:

# MANDATORY:

"current_user_url": "https://api.github.com/user",
"current_user_authorizations_html_url": "https://github.com/settings/connections/applications{/client_id}",
"organization_url": "https://api.github.com/orgs/{org}",
"repository_url": "https://api.github.com/repos/{owner}/{repo}",
"repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}",

# OPTIONAL:
