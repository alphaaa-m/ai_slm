"""Import every model here so Alembic autogenerate sees them."""
from app.models.base import Base  # noqa: F401
from app.models.chat_message import ChatMessage  # noqa: F401
from app.models.course import Course  # noqa: F401
from app.models.document import Document  # noqa: F401
from app.models.question import Question  # noqa: F401
from app.models.quiz_result import QuizResult  # noqa: F401
from app.models.study_kit import StudyKit  # noqa: F401
from app.models.study_session import StudySession  # noqa: F401
from app.models.task import Task  # noqa: F401
from app.models.user import User  # noqa: F401
