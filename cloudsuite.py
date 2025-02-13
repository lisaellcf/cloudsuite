import psutil
import time
import ctypes
import platform

class CloudSuite:
    def __init__(self, bandwidth_limit):
        self.bandwidth_limit = bandwidth_limit
        self.network_interface = self.get_default_network_interface()

    def get_default_network_interface(self):
        addrs = psutil.net_if_addrs()
        return list(addrs.keys())[0]

    def get_network_usage(self):
        net_io = psutil.net_io_counters(pernic=True)
        interface_io = net_io[self.network_interface]
        return interface_io.bytes_sent, interface_io.bytes_recv

    def control_bandwidth(self):
        sent, recv = self.get_network_usage()
        total_usage = (sent + recv) / (1024 ** 2)  # Convert bytes to MB
        print(f"Current total network usage: {total_usage:.2f} MB")

        if total_usage > self.bandwidth_limit:
            self.warn_user(total_usage)

    def warn_user(self, current_usage):
        warning_message = (
            f"Warning: High Network Usage!\n"
            f"Current usage: {current_usage:.2f} MB\n"
            f"Limit: {self.bandwidth_limit} MB\n"
            f"Please reduce your bandwidth consumption."
        )
        print(warning_message)
        self.show_warning_popup(warning_message)

    def show_warning_popup(self, message):
        if platform.system() == "Windows":
            ctypes.windll.user32.MessageBoxW(0, message, "CloudSuite Alert", 1)

    def run(self, check_interval=60):
        try:
            while True:
                self.control_bandwidth()
                time.sleep(check_interval)
        except KeyboardInterrupt:
            print("CloudSuite monitoring stopped.")

if __name__ == "__main__":
    # Example usage: Set bandwidth limit to 500 MB
    bandwidth_limit_mb = 500
    cloud_suite = CloudSuite(bandwidth_limit_mb)
    cloud_suite.run(check_interval=60)