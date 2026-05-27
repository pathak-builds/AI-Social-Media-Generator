"""
Prompt Engineering Module
Builds optimized prompts for different social platforms.
"""

def build_prompt(topic, platform, tone, length):

    platform_rules = {
        "LinkedIn": """
        Write a professional and informative LinkedIn post.
        Focus on insights and value.
        Include relevant hashtags.
        """,

        "Instagram": """
        Write an engaging Instagram caption.
        Use emojis.
        Include trendy hashtags.
        """,

        "Twitter/X": """
        Write a concise Twitter/X post.
        Keep it short and impactful.
        """,

        "Facebook": """
        Write a conversational Facebook post.
        Encourage community engagement.
        """
    }

    length_rules = {
        "Short": "50-80 words",
        "Medium": "100-150 words",
        "Long": "200-300 words"
    }

    prompt = f"""
You are an expert Social Media Content Creator.

Topic:
{topic}

Platform:
{platform}

Tone:
{tone}

Length:
{length_rules[length]}

Instructions:
{platform_rules[platform]}

Generate:

1. Main Post
2. 10 Relevant Hashtags
3. CTA (Call To Action)
4. Alternative Version

Return clean formatted output.
"""

    return prompt

