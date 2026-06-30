// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robot_interfaces:srv/CreateFolder.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "robot_interfaces/srv/create_folder.hpp"


#ifndef ROBOT_INTERFACES__SRV__DETAIL__CREATE_FOLDER__BUILDER_HPP_
#define ROBOT_INTERFACES__SRV__DETAIL__CREATE_FOLDER__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robot_interfaces/srv/detail/create_folder__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_CreateFolder_Request_folder_name
{
public:
  Init_CreateFolder_Request_folder_name()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robot_interfaces::srv::CreateFolder_Request folder_name(::robot_interfaces::srv::CreateFolder_Request::_folder_name_type arg)
  {
    msg_.folder_name = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::CreateFolder_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::CreateFolder_Request>()
{
  return robot_interfaces::srv::builder::Init_CreateFolder_Request_folder_name();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_CreateFolder_Response_message
{
public:
  explicit Init_CreateFolder_Response_message(::robot_interfaces::srv::CreateFolder_Response & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::srv::CreateFolder_Response message(::robot_interfaces::srv::CreateFolder_Response::_message_type arg)
  {
    msg_.message = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::CreateFolder_Response msg_;
};

class Init_CreateFolder_Response_success
{
public:
  Init_CreateFolder_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CreateFolder_Response_message success(::robot_interfaces::srv::CreateFolder_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_CreateFolder_Response_message(msg_);
  }

private:
  ::robot_interfaces::srv::CreateFolder_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::CreateFolder_Response>()
{
  return robot_interfaces::srv::builder::Init_CreateFolder_Response_success();
}

}  // namespace robot_interfaces


namespace robot_interfaces
{

namespace srv
{

namespace builder
{

class Init_CreateFolder_Event_response
{
public:
  explicit Init_CreateFolder_Event_response(::robot_interfaces::srv::CreateFolder_Event & msg)
  : msg_(msg)
  {}
  ::robot_interfaces::srv::CreateFolder_Event response(::robot_interfaces::srv::CreateFolder_Event::_response_type arg)
  {
    msg_.response = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robot_interfaces::srv::CreateFolder_Event msg_;
};

class Init_CreateFolder_Event_request
{
public:
  explicit Init_CreateFolder_Event_request(::robot_interfaces::srv::CreateFolder_Event & msg)
  : msg_(msg)
  {}
  Init_CreateFolder_Event_response request(::robot_interfaces::srv::CreateFolder_Event::_request_type arg)
  {
    msg_.request = std::move(arg);
    return Init_CreateFolder_Event_response(msg_);
  }

private:
  ::robot_interfaces::srv::CreateFolder_Event msg_;
};

class Init_CreateFolder_Event_info
{
public:
  Init_CreateFolder_Event_info()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_CreateFolder_Event_request info(::robot_interfaces::srv::CreateFolder_Event::_info_type arg)
  {
    msg_.info = std::move(arg);
    return Init_CreateFolder_Event_request(msg_);
  }

private:
  ::robot_interfaces::srv::CreateFolder_Event msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robot_interfaces::srv::CreateFolder_Event>()
{
  return robot_interfaces::srv::builder::Init_CreateFolder_Event_info();
}

}  // namespace robot_interfaces

#endif  // ROBOT_INTERFACES__SRV__DETAIL__CREATE_FOLDER__BUILDER_HPP_
