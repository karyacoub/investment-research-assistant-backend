# Investment Research Assistant (IRA) Backend
An LLM-driven asssitant that helps you invest smarter.

## Prerequisites
 * Python 3.12
 * [Ollama](https://ollama.com/download) installed and running

## Local Setup
 1. Download and install [Ollama](https://ollama.com/download) for your chosen platform.
 2. Ensure that Ollama is running in the background.
 3. Pull the correct LLM using the Ollama CLI tool in your terminal:
    ```
    ollama pull gemma3:12b
    ```
 4. Create an Alpha Vantage API key
    * Sign up at [Alpha Vantage](https://www.alphavantage.co/?utm_source=chatgpt.com) for a free API key.
    * Set the API key as an environment variable:
    ```
    export ALPHA_VANTAGE_API_KEY="<YOUR_API_KEY>"
    ```
 5. Install Python dependencies
    ```
    cd <project-directory>
    pipenv shell
    ```

## Running the Backend
In the project directory, run the following:
```
fastapi dev src/main.py
```
> **Note**: The free tier of the Alpha Vantage API only allows up to 25 API calls a day. You can set the `mock` parameter in the request body to bypass the API and LLM calls and return a sample response for testing purposes.

## API
There is one API endpoint set up to use the backend:
 | URI     | Method | Request Body Param | Type    | Description                                                                                                                 |
|---------|--------|--------------------|---------|-----------------------------------------------------------------------------------------------------------------------------|
| /prompt | POST   | prompt             | String  | Prompt from the user to be passed to the LLM agent for processing.                                                          |
|         |        | mock               | Boolean | Default to mock responses to bypass LLM and Alpha Vantage API calls to stay under the free API limit (for testing purposes) |

## Sample Request (cURL)
```
curl --request POST \
  --url http://127.0.0.1:8000/prompt \
  --header 'content-type: application/json' \
  --data '{
  "prompt": "How might Nvidia’s earnings affect semiconductor ETFs?",
  "mock": false
}'
```
> **Note**: As the LLM is running locally, it typically takes between 45 and 60 seconds for the response to return from the backend on my M4 Macbook (YMMV).