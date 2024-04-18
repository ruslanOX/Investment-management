from jira import JIRA
import os
from openai import OpenAI
import requests
from pyairtable import Api

saas_services = [
    {
        'name': 'Jira',
        'category': 'Project Management',
        'users': 10000,
        'pricing_model': 'Subscription',
        'Description': 'This application uses JiraApi',
        'Domain': 'www.atlassian.net/software/jira',
    },
    {
        'name': 'Slack',
        'category': 'Team Collaboration',
        'users': 500000,
        'pricing_model': 'Freemium',
        'Description': 'This application uses slack_sdk',
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

jira = JIRA('https://jira.atlassian.com')

issue = jira.issue('JRA-9')
print(issue.fields.issuetype.name)         # 'New Feature'
print(issue.fields.reporter.displayName)   # 'Mike Cannon-Brookes [Atlassian]'

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

def login(request):
        token = os.getenv("HUBSPOT_API_TOKEN")
        response = requests.get("{0}/{1}".format("https://api.hubapi.com/oauth/v1/access-tokens", token))
        return response.json()

api = Api(os.environ['AIRTABLE_API_KEY'])
table = api.table('appExampleBaseId', 'tblExampleTableId')
table.all()
