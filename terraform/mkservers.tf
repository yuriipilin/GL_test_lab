provider "google" {
 credentials = file("key.json")
 project     = "peppy-ridge-293814"
 region      = "europe-north1"
}

resource "google_compute_instance" "default" {
  name         = "webserver-centos"
  machine_type = "n1-standard-1"
  zone         = "europe-north1-a"

  
  boot_disk {
    initialize_params {
      image = "centos-cloud/centos-8"
    }
  }

  network_interface {
    network = "default"
    
    access_config {
      
    }
  }



  metadata_startup_script = "sudo yum -yq install httpd && sudo systemctl enable httpd && sudo systemctl start httpd"
  
 } 
 
  

 resource "google_compute_instance" "default-1" {
  name         = "webserver-debi"
  machine_type = "n1-standard-1"
  zone         = "europe-north1-a"

  
  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-10"
    }
  }

  network_interface {
    network = "default"
    
    access_config {
      
    }
  }



  metadata_startup_script = "sudo apt update && sudo apt install -y wget && sudo apt install -y apache2"
  
  
  }
