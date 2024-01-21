saas_services = [
    {
        'name': 'Jira',
        'category': 'Project Management',
        'users': 10000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Jira',
        'Domain': 'www.atlassian.net/software/jira',
    },
    {
        'name': 'Slack',
        'category': 'Team Collaboration',
        'users': 500000,
        'pricing_model': 'Freemium',
        'Description': 'This application uses Slack',
        'Domain': 'api.slack.com',
    },
    {
        'name': 'Airtable',
        'category': 'Data',
        'users': 200000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Airtable',
        'Domain': 'www.airtable.com',
    },
    {
        'name': 'Mailchimp',
        'category': 'Mail service',
        'users': 150000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Mailchimp',
        'Domain': 'mailchimp.com',
    },
    {
        'name': 'Dropbox',
        'category': 'File Hosting',
        'users': 30000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Dropbox',
        'Domain': 'www.dropbox.com',
    }
]

# Accessing properties of the first SaaS service (Jira)
print("Name:", saas_services[0]['name'])
print("Category:", saas_services[0]['category'])
print("Users:", saas_services[0]['users'])
print("Pricing Model:", saas_services[0]['pricing_model'])
print("Description:", saas_services[0]['Description'])
print("Domain:", saas_services[0]['Domain'])
