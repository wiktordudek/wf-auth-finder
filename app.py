# ruff: noqa: D103, G004, TRY400
import json
import logging

import psutil
from PyMemoryEditor import OpenProcess

from constants import (
    ACCOUNT_ID_EXPECTED_LENGTH,
    ACCOUNT_ID_PATTERN,
    NONCE_EXPECTED_LENGTH,
    NONCE_PATTERN,
    PROCESS_NAME,
)
from exceptions import GameProcessNotFoundError, MemoryValueNotFoundError
from log import CustomFormatter


def find_game_process(name) -> psutil.Process:
    for process in psutil.process_iter():
        if process.name() == name:
            return process
    raise GameProcessNotFoundError


def read_memory_value(process_pid: int, pattern: str, length: int) -> bytes:
    pattern_bytes = pattern.encode("utf-8")
    with OpenProcess(pid=process_pid) as process:
        for address in process.search_by_value(
            pytype=str, bufflength=len(pattern_bytes), value=pattern_bytes
        ):
            return process.read_process_memory(
                address + len(pattern_bytes), bytes, length
            )
    raise MemoryValueNotFoundError(pattern)


def setup_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    color_handler = logging.StreamHandler()
    color_handler.setFormatter(CustomFormatter())
    logger.addHandler(color_handler)
    return logger


if __name__ == "__main__":
    logger = setup_logger()

    logger.info("🚀 Starting...")
    try:
        game_process = find_game_process(PROCESS_NAME)
        game_pid = game_process.pid
    except GameProcessNotFoundError:
        logger.error("❌ Couldn't find the game process.")
        raise
    except MemoryValueNotFoundError as e:
        logger.error(f"❌ Couldn't find the {e.pattern} value.")
        raise
    except Exception:
        logger.exception("❌ Unexpected error occurred")
        raise

    logger.info(f"🎮 Found the game PID: {game_pid}")

    nonce_data = read_memory_value(
        game_pid,
        NONCE_PATTERN,
        NONCE_EXPECTED_LENGTH,
    )

    account_id_data = read_memory_value(
        game_pid,
        ACCOUNT_ID_PATTERN,
        ACCOUNT_ID_EXPECTED_LENGTH,
    )

    data = {
        "accountId": account_id_data.decode(),
        "nonce": nonce_data.decode(),
    }
    logger.info("✅ Data extracted successfully:")
    print(json.dumps(data, indent=4))
