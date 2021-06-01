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
    )]

FINISH_PAGE = [FinishPage()]

PAGE_ORDER = [RED_BOT_TASK_LIST]
random.shuffle(PAGE_ORDER)
TASKS_LIST = []
for sublist in PAGE_ORDER:
    for s_page in sublist:
        TASKS_LIST.append(s_page)
task_build = PRE_SURVEY_LIST + TASKS_LIST + FINISH_PAGE