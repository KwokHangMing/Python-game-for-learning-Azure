resource "google_storage_bucket_object" "function" {
  count  = length(fileset(path.module, "functions/*"))
  name   = "NPC_messages/function-${count.index + 1}-source.zip"
  bucket = google_storage_bucket.bucket.name
  source = "functions.zip"
}

resource "google_cloudfunctions_function" "npc_vertexai" {
  name        = "npc-messages-dev"
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

resource "google_cloudfunctions_function_iam_member" "invoker_for_npc_vertexai" {
  project        = google_cloudfunctions_function.npc_vertexai.project
  region         = google_cloudfunctions_function.npc_vertexai.region
  cloud_function = google_cloudfunctions_function.npc_vertexai.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}
