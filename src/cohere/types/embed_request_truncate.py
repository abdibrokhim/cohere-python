# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmbedRequestTruncate(str, enum.Enum):
    """
    One of `NONE|START|END` to specify how the API will handle inputs longer than the maximum token length.

    Passing `START` will discard the start of the input. `END` will discard the end of the input. In both cases, input is discarded until the remaining input is exactly the maximum input token length for the model.

    If `NONE` is selected, when the input exceeds the maximum input token length an error will be returned.
    """

    NONE = "NONE"
    START = "START"
    END = "END"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        start: typing.Callable[[], T_Result],
        end: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmbedRequestTruncate.NONE:
            return none()
        if self is EmbedRequestTruncate.START:
            return start()
        if self is EmbedRequestTruncate.END:
            return end()
