import logging
import sys

class LogMaker:
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=".\\logs\\RSPROwebsite.log",
            filemode="w",
            format="%(asctime)s: %(levelname)s: %(message)s",
            datefmt="%d/%m/%Y %H:%M:%S",
            force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        console_handler = logging.StreamHandler(stream=sys.stdout)
        console_handler.setLevel(logging.INFO)

        class NeonFormatter(logging.Formatter):
            COLORS = {
                "INFO": "\033[38;2;57;255;20m",      # Neon Lime
                "PASS":  "\033[38;2;0;255;0m",       # Neon Green
                "ERROR":  "\033[91m",                # Red
                "RESET":   "\033[0m"}

            def format(self, record):
                color = self.COLORS.get(record.levelname, self.COLORS["RESET"])
                message = super().format(record)
                return f"{color}{message}{self.COLORS['RESET']}"

        console_formatter = NeonFormatter("%(asctime)s: %(levelname)s: %(message)s","%H:%M:%S")
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

        def passed(msg):
            logger.info(f"PASS: {msg}")

        def failed(msg):
            logger.error(f"FAIL: {msg}")

        logger.passed = passed
        logger.failed = failed

        return logger
