# Stories
# 1
# AI Story Generator with CrewAI

An automated story generation system that uses CrewAI to create illustrated storybooks. The system employs multiple AI agents working together to outline, write, edit, illustrate, format, and convert stories into PDF documents.

## Features

- **Multi-Agent System**: Utilizes 6 specialized AI agents for different aspects of story creation
- **Automatic Image Generation**: Creates chapter illustrations using OpenAI's DALL-E 3
- **Multiple Genres**: Supports both children's storybooks and science fiction novels
- **Professional Output**: Generates formatted markdown and PDF documents
- **Customizable**: Easy to modify for different story themes and styles

## Prerequisites

- Python 3.8+
- OpenAI API key (for GPT-4 and DALL-E 3)
- Groq API key (optional, for using Groq's LLM endpoints)
- mdpdf installed (`pip install mdpdf`)

## Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [your-repo-name]
```

2. Install required dependencies:
```bash
pip install crewai crewai-tools langchain-openai openai requests mdpdf
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export GROQ_API_KEY="your-groq-api-key"  # Optional
```

## Usage

### For Children's Storybooks (about space ships):
```bash
python app.py
```

### For Science Fiction Novels:
```bash
python app1.py
```

The system will automatically:
1. Create a story outline with 5 chapters
2. Write the full story content (500 words per chapter)
3. Edit and refine the content
4. Generate unique illustrations for each chapter
5. Format everything in markdown
6. Convert to a PDF document

## Project Structure

```
.
├── app.py              # Main application for children's storybooks
├── app1.py             # Application variant for science fiction novels
├── template.md         # Markdown template for story formatting
├── story.md            # Generated story output
├── story.pdf           # Final PDF output
├── mdpdf.log          # Conversion log file
├── sphere1.py         # VPython simulation (bonus content)
└── README.MD          # This file
```

## How It Works

### AI Agents

1. **Story Outliner**: Creates the story structure, chapter titles, and character descriptions
2. **Story Writer**: Writes the full content for all chapters based on the outline
3. **Story Editor**: Refines grammar, punctuation, and style
4. **Image Generator**: Creates chapter illustrations using DALL-E 3
5. **Content Formatter**: Formats the story in markdown with embedded images
6. **PDF Converter**: Converts the final markdown to PDF

### Process Flow

The agents work sequentially:
```
Outline → Write → Edit → Generate Images → Format → Convert to PDF
```

## Configuration

### Changing the LLM Provider

In `app.py` or `app1.py`, modify the `llm` configuration:

```python
llm = ChatOpenAI(
    openai_api_base="https://api.openai.com/v1",  # OpenAI
    # openai_api_base="https://api.groq.com/openai/v1",  # Groq
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-4-turbo-preview"  # or "mixtral-8x7b-32768" for Groq
)
```

### Customizing Story Themes

Modify the agent goals and task descriptions to change:
- Story genre (fantasy, mystery, adventure, etc.)
- Target audience (age groups)
- Chapter count
- Word count per chapter

### Image Style Customization

Edit the DALL-E prompt in the `generateimage` function to change illustration styles:
- Children's books: Whimsical, colorful, storybook illustrations
- Science fiction: Realistic, technology-focused, dramatic lighting

## Known Issues

1. **Image Path Errors**: The mdpdf converter may have issues with absolute file paths on Windows. The log shows errors like:
   ```
   ERROR: C:\Users\...\chapter_1_awakening_in_orbit.png: No such file or directory
   ```
   
   **Solution**: Ensure images are saved with relative paths or adjust the markdown image references.

2. **API Rate Limits**: Generating multiple images quickly may hit OpenAI rate limits. Consider adding delays between image generations if needed.

## Output Examples

### Generated Files

- **story.md**: Markdown file with formatted story and image references
- **story.pdf**: Final PDF document with embedded images
- **[chapter_name].png**: Individual chapter illustrations

### Sample Story Structure

```markdown
# [Story Title]

## Chapter 1: [Chapter Title]
![Chapter 1 Image](path/to/image1.png)
[Chapter content...]

## Chapter 2: [Chapter Title]
![Chapter 2 Image](path/to/image2.png)
[Chapter content...]
```

## Tips for Best Results

1. **API Keys**: Ensure your OpenAI API key has access to both GPT-4 and DALL-E 3
2. **Image Generation**: Be patient - image generation can take 10-20 seconds per image
3. **Customization**: Experiment with different prompts and agent descriptions for varied results
4. **Error Handling**: Check the mdpdf.log file if PDF conversion fails

## Bonus Content

The project includes `sphere1.py`, a VPython simulation of bouncing balls in a sphere. Run it separately for a fun physics visualization:

```bash
pip install vpython
python sphere1.py
```

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

[Add your license information here]

## Acknowledgments

- Built with [CrewAI](https://crewai.com/)
- Images generated using OpenAI's DALL-E 3
- PDF conversion using mdpdf