#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to robot_interfaces__srv__CreateFolder_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CreateFolder_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub folder_name: std::string::String,

}



impl Default for CreateFolder_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::CreateFolder_Request::default())
  }
}

impl rosidl_runtime_rs::Message for CreateFolder_Request {
  type RmwMsg = super::srv::rmw::CreateFolder_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        folder_name: msg.folder_name.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        folder_name: msg.folder_name.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      folder_name: msg.folder_name.to_string(),
    }
  }
}


// Corresponds to robot_interfaces__srv__CreateFolder_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CreateFolder_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub message: std::string::String,

}



impl Default for CreateFolder_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::CreateFolder_Response::default())
  }
}

impl rosidl_runtime_rs::Message for CreateFolder_Response {
  type RmwMsg = super::srv::rmw::CreateFolder_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
        message: msg.message.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
        message: msg.message.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
      message: msg.message.to_string(),
    }
  }
}






#[link(name = "robot_interfaces__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__robot_interfaces__srv__CreateFolder() -> *const std::ffi::c_void;
}

// Corresponds to robot_interfaces__srv__CreateFolder
#[allow(missing_docs, non_camel_case_types)]
pub struct CreateFolder;

impl rosidl_runtime_rs::Service for CreateFolder {
    type Request = CreateFolder_Request;
    type Response = CreateFolder_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__robot_interfaces__srv__CreateFolder() }
    }
}


