# Deploy AWS infra using Azure repo, pipelines

## Purpose

Using Azure repo and pipelines, deploy the aws infrastructure using IAM credentials. The code is used here, *aws cdk python*.

## Pre-requisites

- AWS [CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html).
- AWS [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) credentials.
- AWS [plugin](https://marketplace.visualstudio.com/search?term=aws&target=AzureDevOps&category=All%20categories&sortBy=Relevance) in Azure DevOps (*Which helps on making service connection under auzure devops project*).![alt text](<pics/Screenshot 2024-11-29 at 15.32.57.png>)
- Select the DevOps to install.

## Implementation

- Create Azure repo. Clone it. empty one.
- Inititate the cdk project. Eg. ```cdk init app --language python```
- Add the below code to deploy/azure_pipeline.yml

```
trigger:
- main
- master

pool:
  vmImage: 'ubuntu-latest'

steps:
- task: UsePythonVersion@0
  inputs:
    versionSpec: '3.x'
    addToPath: true

- script: |
    npm install -g aws-cdk
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt
  displayName: 'Install dependencies'
- script: |
    source .venv/bin/activate
    cdk bootstrap aws://$(AWS_ACCOUNT_ID)/$(AWS_DEFAULT_REGION)
  displayName: 'Bootstrap AWS account'
  env:
    AWS_ACCESS_KEY_ID: $(AWS_ACCESS_KEY_ID)
    AWS_SECRET_ACCESS_KEY: $(AWS_SECRET_ACCESS_KEY)
    AWS_DEFAULT_REGION: $(AWS_DEFAULT_REGION)
# - task: AWSCLI@1
#   inputs:
#     awsCredentials: 'azuredevopsaws'
#     regionName: 'eu-central-1'
#     scriptType: 'inline'
#     inlineScript: |
#       cdk synth
#   displayName: 'Synth CDK stack'

- script: |
    source .venv/bin/activate
    cdk synth
    cdk deploy --require-approval never
  displayName: 'Deploy CDK stack'
  env:
    AWS_ACCESS_KEY_ID: $(AWS_ACCESS_KEY_ID)
    AWS_SECRET_ACCESS_KEY: $(AWS_SECRET_ACCESS_KEY)
    AWS_DEFAULT_REGION: $(AWS_DEFAULT_REGION)
```
- Creating the service connection:
    - Go to -> Project settings -> click: service connection -> select: AWS plugin -> add aws IAM user access and secret keys.![alt text](<pics/Screenshot 2024-12-02 at 10.30.22.png>)
    - Give a name and add AWS IAM User *Access* and *Secret* keys.
    - Create the pipeline using Azure repo.
    - Add the variables/keys shown below:![alt text](<pics/Screenshot 2024-12-02 at 11.21.01.png>)
    - Save it.