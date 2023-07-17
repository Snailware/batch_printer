from datetime import datetime, timedelta, tzinfo

from pytz import timezone


class Timer:
    def __init__(self, tz: str = "EST") -> None:
        self.time_zone: tzinfo = timezone(tz)
        self.start_time: datetime = None
        self.stop_time: datetime = None

    def start(self) -> datetime:
        self.start_time = datetime.now(self.time_zone)
        return self.start_time

    def stop(self) -> datetime:
        self.stop_time = datetime.now(self.time_zone)
        return self.stop_time

    def elapsed_time(self) -> timedelta:
        if self.start_time is None:
            raise Exception(
                "start_time has not been set. Use Timer.start() to create start point."
            )
        elif self.stop_time is None:
            raise Exception(
                "stop_time has not been set. Use Timer.stop() to create stop point."
            )
        else:
            return self.stop_time - self.start_time

    def verbose_elapsed_time(self) -> str:
        verbose_time = ""
        elapsed_time = self.elapsed_time()
        elapsed_minutes = int(elapsed_time.total_seconds() / 60)
        elapsed_seconds = int(elapsed_time.total_seconds() % 60)
        if elapsed_minutes > 0:
            verbose_time += f"{elapsed_minutes} min"
        if elapsed_minutes > 0 and elapsed_seconds > 0:
            verbose_time += " "
        if elapsed_seconds > 0:
            verbose_time += f"{elapsed_seconds} sec"
        return verbose_time


if __name__ == "__main__":
    print("this file should not be run directly. it contains code used by other files.")
