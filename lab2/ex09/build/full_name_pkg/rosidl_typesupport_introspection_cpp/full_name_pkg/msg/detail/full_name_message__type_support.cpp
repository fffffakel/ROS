// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from full_name_pkg:msg/FullNameMessage.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "full_name_pkg/msg/detail/full_name_message__functions.h"
#include "full_name_pkg/msg/detail/full_name_message__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace full_name_pkg
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void FullNameMessage_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) full_name_pkg::msg::FullNameMessage(_init);
}

void FullNameMessage_fini_function(void * message_memory)
{
  auto typed_message = static_cast<full_name_pkg::msg::FullNameMessage *>(message_memory);
  typed_message->~FullNameMessage();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember FullNameMessage_message_member_array[3] = {
  {
    "last_name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_pkg::msg::FullNameMessage, last_name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_pkg::msg::FullNameMessage, name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "first_name",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is key
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(full_name_pkg::msg::FullNameMessage, first_name),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers FullNameMessage_message_members = {
  "full_name_pkg::msg",  // message namespace
  "FullNameMessage",  // message name
  3,  // number of fields
  sizeof(full_name_pkg::msg::FullNameMessage),
  false,  // has_any_key_member_
  FullNameMessage_message_member_array,  // message members
  FullNameMessage_init_function,  // function to initialize message memory (memory has to be allocated)
  FullNameMessage_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t FullNameMessage_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &FullNameMessage_message_members,
  get_message_typesupport_handle_function,
  &full_name_pkg__msg__FullNameMessage__get_type_hash,
  &full_name_pkg__msg__FullNameMessage__get_type_description,
  &full_name_pkg__msg__FullNameMessage__get_type_description_sources,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace full_name_pkg


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<full_name_pkg::msg::FullNameMessage>()
{
  return &::full_name_pkg::msg::rosidl_typesupport_introspection_cpp::FullNameMessage_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, full_name_pkg, msg, FullNameMessage)() {
  return &::full_name_pkg::msg::rosidl_typesupport_introspection_cpp::FullNameMessage_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
