import os
import openai
import config

openai.api_key = config.OPENAI_API_KEY


def generateBlogTopics(prompt1):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="Generate blog topics on: {}. \n \n 1.  ".format(prompt1),
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response['choices'][0]['text']


def generateBlogSections(prompt1):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt1),
        temperature=0.6,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text'].split("\n-")


def blogSectionExpander(prompt1):
    response = openai.Completion.create(
        engine="davinci-instruct-beta-v3",
        prompt="Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(
            prompt1),
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


def generateBlog(topic):
    blogArticle = ""
    sections = generateBlogSections(topic)
    intro = blogSectionExpander(topic)
    sectionContent = [blogSectionExpander(section) for section in sections]
    blogArticle += "<h1>" + topic + "</h1>"
    for index, section in enumerate(sections):
        if section:
            blogArticle += "<h2>"+section+"</h2>"
        if sectionContent[index]:
            blogArticle += "<p>"+sectionContent[index].replace('\n', '<br>')+"</p><br>"

    return blogArticle


