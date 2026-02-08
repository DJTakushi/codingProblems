#include "utility.hpp"

#include <functional>
#include <thread>
#include <chrono>
#include <future>

using namespace std::chrono_literals;

void Utility::CheckTimeout(std::function<void()> func, int timeout_in_milliseconds) {
  std::packaged_task<void()> task(func);
  auto future = task.get_future();
  std::thread thr(std::move(task));
  if (future.wait_for(std::chrono::milliseconds(timeout_in_milliseconds)) != std::future_status::timeout) {
    thr.join();
    future.get();
  }
  else {
    thr.detach();
    throw std::runtime_error(
      "  The method failed to execute within a timeout of " + std::to_string(timeout_in_milliseconds) + "ms"
    );
  }
}
