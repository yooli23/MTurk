from utils.build_utils import (
    Page,
    WelcomePage,
    FinishPage,
)

from utils.build_utils import (
    Form,
    Section,
    FreeResponse,
    MultiChoice,
    CheckBox,
    Likert,
)

from utils.build_utils import (
    Task,
    Agent,
    AgentColor,
)
import random

PRE_SURVEY_LIST = [WelcomePage()]

CYAN_BOT_TASK_LIST = [Task(
        """
        1. <b>Chat naturally</b> as to a friend, talking about your movie history, preference, and/or your partner's movie recommendation.

        2.  When a bot recommends a movie. you can type in <b>[accept]</b> to accept the recommendation, or you can continue the chat if you don't get a good recommendation.

        3. If the response is bad and you can't continue the chat, you can type in <b>[quit]</b> to end the chat.

        4. Please don’t game the task by replying short and meaningless sentences. Discuss more about the movies (what you like, acting, experience, etc.)

        5. You can click <b>Complete Chat</b> when you <b>finish the chat</b>.

        """,
        Agent(
            color=AgentColor.CYAN,
            name='cyan',
            title='CyanBot',
        ),
    ),

    Form("Post Task Survey Cyan Bot",
        Section("",
            MultiChoice(
                title="Did Cyan Bot recommend a movie to you?",
                items=["Yes", "No"]
            ),

            MultiChoice(
                title="If Cyan Bot recommended a movie to you, does the movie recommendation fit your personal preferences?",
                items=["Cyan Bot recommended a movie and it fits my personal preferences.",
                 "Cyan Bot recommended a movie but it doesn't fit my personal preferences.",
                 "Cyan Bot didn't recommend a movie."]
            ),
            MultiChoice(
                title="How consistent was the conversation? 1 (many inconsistent statements) -- 5 (very consistent)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How natural was the conversation? 1 (many unnatural statements) -- 5 (very natural)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How engaging was the conversation? 1 (not engaging at all) -- 5 (very engaging)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How persuasive was your partner? 1 (not persuasive at all) -- 5 (very persuasive)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How sociable was your partner? 1 (not sociable at all) -- 5 (very sociable)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How boring was the conversation? 1 (not boring at all) -- 5 (very boring)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
        ),
    ),]

YELLOW_BOT_TASK_LIST = [Task(
        """
        1. <b>Chat naturally</b> as to a friend, talking about your movie history, preference, and/or your partner's movie recommendation.

        2.  When a bot recommends a movie. you can type in <b>[accept]</b> to accept the recommendation, or you can continue the chat if you don't get a good recommendation.

        3. If the response is bad and you can't continue the chat, you can type in <b>[quit]</b> to end the chat.

        4. Please don’t game the task by replying short and meaningless sentences. Discuss more about the movies (what you like, acting, experience, etc.)

        5. You can click <b>Complete Chat</b> when you <b>finish the chat</b>.

        """,
        Agent(
            color=AgentColor.YELLOW,
            name='yellow',
            title='YellowBot',
        ),
    ),

    Form("Post Task Survey Yellow Bot",
        Section("",
            MultiChoice(
                title="Did Yellow Bot recommend a movie to you?",
                items=["Yes", "No"]
            ),

            MultiChoice(
                title="If Yellow Bot recommended a movie to you, does the movie recommendation fit your personal preferences?",
                items=["Yellow Bot recommended a movie and it fits my personal preferences.",
                 "Yellow Bot recommended a movie but it doesn't fit my personal preferences.",
                 "Yellow Bot didn't recommend a movie."]
            ),
            MultiChoice(
                title="How consistent was the conversation? 1 (many inconsistent statements) -- 5 (very consistent)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How natural was the conversation? 1 (many unnatural statements) -- 5 (very natural)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How engaging was the conversation? 1 (not engaging at all) -- 5 (very engaging)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How persuasive was your partner? 1 (not persuasive at all) -- 5 (very persuasive)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How sociable was your partner? 1 (not sociable at all) -- 5 (very sociable)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How boring was the conversation? 1 (not boring at all) -- 5 (very boring)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
        ),
    ),]

GREEN_BOT_TASK_LIST = [Task(
        """
        1. <b>Chat naturally</b> as to a friend, talking about your movie history, preference, and/or your partner's movie recommendation.

        2.  When a bot recommends a movie. you can type in <b>[accept]</b> to accept the recommendation, or you can continue the chat if you don't get a good recommendation.

        3. If the response is bad and you can't continue the chat, you can type in <b>[quit]</b> to end the chat.

        4. Please don’t game the task by replying short and meaningless sentences. Discuss more about the movies (what you like, acting, experience, etc.)

        5. You can click <b>Complete Chat</b> when you <b>finish the chat</b>.

        """,
        Agent(
            color=AgentColor.GREEN,
            name='green',
            title='GreenBot',
        ),
    ),

    Form("Post Task Survey Green Bot",
        Section("",
            MultiChoice(
                title="Did Green Bot recommend a movie to you?",
                items=["Yes", "No"]
            ),

            MultiChoice(
                title="If Green Bot recommended a movie to you, does the movie recommendation fit your personal preferences?",
                items=["Green Bot recommended a movie and it fits my personal preferences.",
                 "Green Bot recommended a movie but it doesn't fit my personal preferences.",
                 "Green Bot didn't recommend a movie."]
            ),
            MultiChoice(
                title="How consistent was the conversation? 1 (many inconsistent statements) -- 5 (very consistent)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How natural was the conversation? 1 (many unnatural statements) -- 5 (very natural)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How engaging was the conversation? 1 (not engaging at all) -- 5 (very engaging)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How persuasive was your partner? 1 (not persuasive at all) -- 5 (very persuasive)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How sociable was your partner? 1 (not sociable at all) -- 5 (very sociable)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How boring was the conversation? 1 (not boring at all) -- 5 (very boring)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
        ),
    ),]

BLUE_BOT_TASK_LIST = [Task(
        """
        1. <b>Chat naturally</b> as to a friend, talking about your movie history, preference, and/or your partner's movie recommendation.

        2.  When a bot recommends a movie. you can type in <b>[accept]</b> to accept the recommendation, or you can continue the chat if you don't get a good recommendation.

        3. If the response is bad and you can't continue the chat, you can type in <b>[quit]</b> to end the chat.

        4. Please don’t game the task by replying short and meaningless sentences. Discuss more about the movies (what you like, acting, experience, etc.)

        5. You can click <b>Complete Chat</b> when you <b>finish the chat</b>.

        """,
        Agent(
            color=AgentColor.BLUE,
            name='blue',
            title='BlueBot',
        ),
    ),   

    Form("Post Task Survey Blue Bot",
        Section("",
            MultiChoice(
                title="Did Blue Bot recommend a movie to you?",
                items=["Yes", "No"]
            ),

            MultiChoice(
                title="If Blue Bot recommended a movie to you, does the movie recommendation fit your personal preferences?",
                items=["Blue Bot recommended a movie and it fits my personal preferences.",
                 "Blue Bot recommended a movie but it doesn't fit my personal preferences.",
                 "Blue Bot didn't recommend a movie."]
            ),
            MultiChoice(
                title="How consistent was the conversation? 1 (many inconsistent statements) -- 5 (very consistent)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How natural was the conversation? 1 (many unnatural statements) -- 5 (very natural)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How engaging was the conversation? 1 (not engaging at all) -- 5 (very engaging)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How persuasive was your partner? 1 (not persuasive at all) -- 5 (very persuasive)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How sociable was your partner? 1 (not sociable at all) -- 5 (very sociable)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How boring was the conversation? 1 (not boring at all) -- 5 (very boring)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
        ),
    ),]

RED_BOT_TASK_LIST = [Task(
        """
        1. <b>Chat naturally</b> as to a friend, talking about your movie history, preference, and/or your partner's movie recommendation.

        2.  When a bot recommends a movie. you can type in <b>[accept]</b> to accept the recommendation, or you can continue the chat if you don't get a good recommendation.

        3. If the response is bad and you can't continue the chat, you can type in <b>[quit]</b> to end the chat.

        4. Please don’t game the task by replying short and meaningless sentences. Discuss more about the movies (what you like, acting, experience, etc.)

        5. You can click <b>Complete Chat</b> when you <b>finish the chat</b>.

        """,
        Agent(
            color=AgentColor.RED,
            name='red',
            title='RedBot',
        ),
    ), 


    Form("Post Task Survey Red Bot",
        Section("",
            MultiChoice(
                title="Did Red Bot recommend a movie to you?",
                items=["Yes", "No"]
            ),

            MultiChoice(
                title="If Red Bot recommended a movie to you, does the movie recommendation fit your personal preferences?",
                items=["Red Bot recommended a movie and it fits my personal preferences.",
                 "Red Bot recommended a movie but it doesn't fit my personal preferences.",
                 "Red Bot didn't recommend a movie."]
            ),
            MultiChoice(
                title="How consistent was the conversation? 1 (many inconsistent statements) -- 5 (very consistent)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How natural was the conversation? 1 (many unnatural statements) -- 5 (very natural)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How engaging was the conversation? 1 (not engaging at all) -- 5 (very engaging)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How persuasive was your partner? 1 (not persuasive at all) -- 5 (very persuasive)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How sociable was your partner? 1 (not sociable at all) -- 5 (very sociable)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
            MultiChoice(
                title="How boring was the conversation? 1 (not boring at all) -- 5 (very boring)",
                items=["1",
                 "2",
                 "3",
                 "4",
                 "5"]
            ),
        ),
    ),]

FINISH_PAGE = [FinishPage()]

PAGE_ORDER = [RED_BOT_TASK_LIST]
random.shuffle(PAGE_ORDER)
TASKS_LIST = []
for sublist in PAGE_ORDER:
    for s_page in sublist:
        TASKS_LIST.append(s_page)
task_build = PRE_SURVEY_LIST + TASKS_LIST + FINISH_PAGE