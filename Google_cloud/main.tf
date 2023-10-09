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

