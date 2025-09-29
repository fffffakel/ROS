// generated from rosidl_typesupport_fastrtps_c/resource/idl__rosidl_typesupport_fastrtps_c.h.em
// with input from full_name_pkg:msg/FullNameMessage.idl
// generated code does not contain a copyright notice
#ifndef FULL_NAME_PKG__MSG__DETAIL__FULL_NAME_MESSAGE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
#define FULL_NAME_PKG__MSG__DETAIL__FULL_NAME_MESSAGE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_


#include <stddef.h>
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "full_name_pkg/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "full_name_pkg/msg/detail/full_name_message__struct.h"
#include "fastcdr/Cdr.h"

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
bool cdr_serialize_full_name_pkg__msg__FullNameMessage(
  const full_name_pkg__msg__FullNameMessage * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
bool cdr_deserialize_full_name_pkg__msg__FullNameMessage(
  eprosima::fastcdr::Cdr &,
  full_name_pkg__msg__FullNameMessage * ros_message);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
size_t get_serialized_size_full_name_pkg__msg__FullNameMessage(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
size_t max_serialized_size_full_name_pkg__msg__FullNameMessage(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
bool cdr_serialize_key_full_name_pkg__msg__FullNameMessage(
  const full_name_pkg__msg__FullNameMessage * ros_message,
  eprosima::fastcdr::Cdr & cdr);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
size_t get_serialized_size_key_full_name_pkg__msg__FullNameMessage(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
size_t max_serialized_size_key_full_name_pkg__msg__FullNameMessage(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_full_name_pkg
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, full_name_pkg, msg, FullNameMessage)();

#ifdef __cplusplus
}
#endif

#endif  // FULL_NAME_PKG__MSG__DETAIL__FULL_NAME_MESSAGE__ROSIDL_TYPESUPPORT_FASTRTPS_C_H_
