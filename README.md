
# YouTube_Content_Optimizer_Crew
=======
# YouTube Content Optimizer Crew

Welcome to the YouTube Content Optimizer Crew project,. This project uses multiple AI agents to optimize your YouTube content metadata, including titles, descriptions, and tags, to maximize visibility and engagement.

## Features

- **Title Generation**: Creates engaging, SEO-optimized titles that drive high CTR
- **Description Optimization**: Crafts comprehensive descriptions with proper formatting and keywords
- **Tag Research**: Identifies and implements the most effective tags for maximum visibility

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

1. First lock the dependencies and then install them:
```bash
uv lock
```
```bash
uv sync
```

### Configuration

1. Add your `OPENAI_API_KEY` into the `.env` file
2. Modify `src/youtube_optimization/config/agents.yaml` to customize agent behaviors
3. Modify `src/youtube_optimization/config/tasks.yaml` to adjust optimization tasks
4. Modify the main scripts to customize input/output handling

## Usage

To optimize your YouTube content, run this from the root folder:

```bash
$ crewai run
```
or
```bash
uv run job_change_monitor
```

The system will generate:
- Multiple optimized title variations
- A comprehensive, SEO-friendly description
- A strategic set of tags for maximum visibility

## Understanding the Crew

The YouTube Content Optimizer Crew consists of three specialized AI agents:

1. **Title Generator**: Creates engaging and SEO-optimized titles
2. **Description Writer**: Crafts comprehensive and engaging video descriptions
3. **Tag Researcher**: Researches and implements optimal tag strategies

Each agent collaborates to ensure your YouTube content has the best chance of success in the algorithm.


>>>>>>> b7c534d (Initial commit)
