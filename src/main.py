from datetime import datetime, timezone


def main() -> None:
    print("insider-threat-behavior-analytics initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
