saas_services = [
    {
        'name': 'Jira',
        'category': 'Project Management',
        'users': 10000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Jira',
    },
    {
        'name': 'Slack',
        'category': 'Team Collaboration',
        'users': 500000,
        'pricing_model': 'Freemium',
        'Description': 'This application uses Slack',
    },
    {
        'name': 'Airtable',
        'category': 'Data',
        'users': 200000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Airtable',
    },
    {
        'name': 'Mailchimp',
        'category': 'Mail service',
        'users': 150000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Mailchimp',
    },
    {
        'name': 'Zendesk',
        'category': 'Customer Support',
        'users': 30000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses Zendesk',
    }
]

# Accessing properties of the first SaaS service (Jira)
print("Name:", saas_services[0]['name'])
print("Category:", saas_services[0]['category'])
print("Users:", saas_services[0]['users'])
print("Pricing Model:", saas_services[0]['pricing_model'])
print("Description:", saas_services[0]['Description'])
