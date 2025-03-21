from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import json

def load_mistral_model(model_path, n_ctx=2048, temperature=0.7):
    """
    Load Mistral LLM model for local inference.
    """
    callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
    llm = LlamaCpp(
        model_path=model_path,
        temperature=temperature,
        max_tokens=n_ctx,
        callback_manager=callback_manager,
        verbose=True
    )
    return llm

def parse_invoice_with_mistral(llm, text, json_schema):
    """
    Parses invoice text into structured JSON format using Mistral.
    """
    from jsonformer.main import Jsonformer
    
    builder = Jsonformer(
        model=llm,
        json_schema=json_schema,
        prompt=text,
        max_string_token_length=30
    )
    return builder()
