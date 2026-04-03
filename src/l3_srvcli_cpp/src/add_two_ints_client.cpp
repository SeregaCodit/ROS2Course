#include <memory>
#include <chrono>
#include <cstdlib>
#include <future> 

#include "example_interfaces/srv/add_two_ints.hpp"
#include "rclcpp/rclcpp.hpp"

using namespace std::chrono_literals;


class AddTwoIntsClient : public rclcpp::Node
{
public:
    AddTwoIntsClient() : Node("add_two_ints_client")
    {
        client_ = this->create_client<example_interfaces::srv::AddTwoInts>(
            "add_two_ints"
        );

        while (!client_->wait_for_service(1s))
        {   
            if (!rclcpp::ok())
            {
                RCLCPP_ERROR(this->get_logger(), "rclcpp in not ok");
                return;
            };         
            RCLCPP_INFO(this->get_logger(), "Waiting for service");
        }
        RCLCPP_INFO(this->get_logger(), "Client initialized!");
    };

    std::shared_future<std::shared_ptr<example_interfaces::srv::AddTwoInts::Response>>
    send_request(int64_t a, int64_t b)
    {
        auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();

        request->a = a;
        request->b = b;
        return client_->async_send_request(request).future.share();
    };

    
private:
    rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr client_;

};

int main(int argc, char * argv[])
{
    if (argc != 3)
    {
        RCLCPP_ERROR(rclcpp::get_logger("rclcpp"), "usage: add_two_ints_client X Y");
        return 1;
    }

    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsClient>();
    int64_t a = atoll(argv[1]);
    int64_t b = atoll(argv[2]);
    auto result_future = node->send_request(a, b);

    if (rclcpp::spin_until_future_complete(node, result_future) == rclcpp::FutureReturnCode::SUCCESS)
    {
        auto response = result_future.get();
        RCLCPP_INFO(node->get_logger(), "%ld + %ld = %ld", a, b, response->sum);
    }else{
        RCLCPP_ERROR(node->get_logger(), "failed to call service");
    }

    rclcpp::shutdown();
    return 0;
};