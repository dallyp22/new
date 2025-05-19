from ..core.logging import logger
from ..risk.manager import ApprovedSignal


async def execute(signal: ApprovedSignal) -> None:
    logger.info("executing order", extra=signal.__dict__)
    # TODO: call Alpaca API
