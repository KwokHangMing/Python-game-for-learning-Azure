terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.84.0"
    }
  }
}

provider "google" {
  # Configuration options
  credentials = (file("credentials.json"))
  project = "final-year-project-400406"
  region  = "us-central1"
}

resource "google_storage_bucket" "bucket" {
  name     = "220011928-bucket"
  location = "US"
}

resource "google_storage_bucket_object" "npc_folder" {
  name   = "NPC_messages/"
  bucket = google_storage_bucket.bucket.name
  content = "npc_folder"
}

resource "google_storage_bucket_object" "archive" {
  name   = "NPC_messages/function-source.zip"
  bucket = google_storage_bucket.bucket.name
  source = "/workspaces/Python-game-for-learning-Azure/Google_cloud/functions.zip"
}

resource "google_cloudfunctions_function" "npc_messages" {
  name        = "npc-messages"
  description = "This function will send messages to the user"
  runtime     = "python39"

  available_memory_mb               = 256
  source_archive_bucket             = google_storage_bucket.bucket.name
  source_archive_object             = google_storage_bucket_object.archive.name
  entry_point                       = "npc_messages"
  trigger_http                      = true
  https_trigger_security_level      = "SECURE_ALWAYS"
  ingress_settings = "ALLOW_ALL"
}

resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = google_cloudfunctions_function.npc_messages.project
  region         = google_cloudfunctions_function.npc_messages.region
  cloud_function = google_cloudfunctions_function.npc_messages.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}
