import cocotb
from cocotb.triggers import Timer
import logging
logger = logging.getLogger("coroutines")
logging.basicConfig(level=logging.NOTSET)
logger.setLevel(logging.INFO)


async def green():
    await red()
    logger.info("GREEN: Traffic going")


async def yellow():
    logger.info("YELLOW: Traffic slowing")
    await Timer(1, units="ns")


async def red():
    await yellow()
    logger.info("RED: Traffic stopped")
    await Timer(2, units="ns")


@cocotb.test()
async def traffic(_):
    """Simulating a traffic light"""
    for _ in range(2):
        await Timer(3, units="ns")
        logger.info("Button pressed")
        await green()
