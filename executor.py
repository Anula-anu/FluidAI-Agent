import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def execute_plan(plan):

    prompt = f"""
You are an AI Business Document Generator.

Using the following execution plan:

{plan}

Generate a professional business document.

The document should contain:

# Title

## Executive Summary

## Introduction

## Solution

## Features

## Benefits

## Implementation Plan

## Conclusion

Write professionally.
"""

    response = model.generate_content(prompt)

    return response.text