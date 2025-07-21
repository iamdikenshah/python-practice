from plyer import notification
import time

def send_simple_notification():
    """Sends a basic desktop notification."""
    notification.notify(
        title='My First Plyer Notification',
        message='Hello from Python! This is a simple desktop notification.',
        app_name='Python Notifier',
        # app_icon='path/to/your/icon.ico',  # Optional: Path to an .ico file for Windows
                                            # or a .png file for Linux/macOS
        timeout=10  # Notification will disappear after 10 seconds
    )

def send_timed_notification():
    """Sends a notification and then waits before sending another."""
    print("Sending first notification...")
    notification.notify(
        title='Timed Notification 1',
        message='This is the first notification. Waiting for 5 seconds...',
        app_name='Timed Notifier',
        timeout=5
    )
    time.sleep(5)  # Wait for 5 seconds

    print("Sending second notification...")
    notification.notify(
        title='Timed Notification 2',
        message='This is the second notification. Hope you saw the first!',
        app_name='Timed Notifier',
        timeout=5
    )

if __name__ == "__main__":
    print("--- Basic Notification Example ---")
    send_simple_notification()
    print("Check your desktop for the notification!")
    time.sleep(2) # Give a moment for the notification to show before moving on

    print("\n--- Timed Notification Example ---")
    send_timed_notification()
    print("Notifications sent. Program finished.")