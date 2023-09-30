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

resource "google_dialogflow_cx_agent" "full_agent" {
  display_name = "dialogflowcx-agent"
  location = "global"
  default_language_code = "en"
  time_zone = "Hong Kong"
  description = "This is a test agent."
  enable_stackdriver_logging = true
  enable_spell_correction    = true
    speech_to_text_settings {
        enable_speech_adaptation = true
    }
}

resource "google_dialogflow_cx_entity_type" "basic_entity_type" {
  parent       = google_dialogflow_cx_agent.full_agent.id
  display_name = "MyEntity"
  kind         = "KIND_MAP"
  entities {
    value = "value1"
    synonyms = ["synonym1","synonym2"]
  }
  entities {
    value = "value2"
    synonyms = ["synonym3","synonym4"]
  }
  enable_fuzzy_extraction = false
} 