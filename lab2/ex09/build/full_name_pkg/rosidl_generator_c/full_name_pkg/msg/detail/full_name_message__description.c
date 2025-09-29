// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from full_name_pkg:msg/FullNameMessage.idl
// generated code does not contain a copyright notice

#include "full_name_pkg/msg/detail/full_name_message__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_full_name_pkg
const rosidl_type_hash_t *
full_name_pkg__msg__FullNameMessage__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x1a, 0xfc, 0x28, 0xf4, 0x69, 0xc7, 0xb3, 0xf9,
      0xc5, 0x6f, 0x91, 0x9f, 0xc5, 0xbd, 0xb0, 0x4b,
      0x09, 0x16, 0x42, 0x52, 0xfb, 0xd9, 0x80, 0xf1,
      0xcf, 0x64, 0x0a, 0x6f, 0xb5, 0x70, 0x22, 0x3b,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char full_name_pkg__msg__FullNameMessage__TYPE_NAME[] = "full_name_pkg/msg/FullNameMessage";

// Define type names, field names, and default values
static char full_name_pkg__msg__FullNameMessage__FIELD_NAME__last_name[] = "last_name";
static char full_name_pkg__msg__FullNameMessage__FIELD_NAME__name[] = "name";
static char full_name_pkg__msg__FullNameMessage__FIELD_NAME__first_name[] = "first_name";

static rosidl_runtime_c__type_description__Field full_name_pkg__msg__FullNameMessage__FIELDS[] = {
  {
    {full_name_pkg__msg__FullNameMessage__FIELD_NAME__last_name, 9, 9},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {full_name_pkg__msg__FullNameMessage__FIELD_NAME__name, 4, 4},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {full_name_pkg__msg__FullNameMessage__FIELD_NAME__first_name, 10, 10},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
full_name_pkg__msg__FullNameMessage__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {full_name_pkg__msg__FullNameMessage__TYPE_NAME, 33, 33},
      {full_name_pkg__msg__FullNameMessage__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string last_name\n"
  "string name\n"
  "string first_name";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
full_name_pkg__msg__FullNameMessage__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {full_name_pkg__msg__FullNameMessage__TYPE_NAME, 33, 33},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 46, 46},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
full_name_pkg__msg__FullNameMessage__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *full_name_pkg__msg__FullNameMessage__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
