#!/usr/bin/env python
import sys

from youtube_optimizer.crew import YouTubeOptimizerCrew

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the YouTube content optimization crew.
    """
    video_info = {
        "title": "How to Build an AI Assistant with Python",
        "content_description": """
        In this comprehensive tutorial, we'll build a powerful AI assistant using Python.
        We'll cover:
        - Setting up the development environment
        - Integrating with OpenAI's GPT models
        - Building a natural language interface
        - Adding custom tools and capabilities
        - Deploying the assistant
        """,
        "target_audience": "Python developers, AI enthusiasts, and software engineers",
        "keywords": ["AI", "Python", "Tutorial", "GPT", "Programming"],
    }
    
    inputs = {
        "video_info": video_info,
        "style": "educational",
        "tone": "professional but approachable"
    }
    
    YouTubeOptimizerCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "YouTube Content Optimization"}
    try:
        YouTubeOptimizerCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        YouTubeOptimizerCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "YouTube Content Optimization"}
    try:
        return YouTubeOptimizerCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
