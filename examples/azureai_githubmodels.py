import os

from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
)

response = client.complete(
    messages=[
        SystemMessage(content="You are a helpful assistant that always responds in markdown with helpful emphasis."),
        UserMessage(content="What is the capital of France?"),
    ],
    model=os.getenv("GITHUB_MODEL", "gpt-4.1"),
)
print(response.choices[0].message.content)
