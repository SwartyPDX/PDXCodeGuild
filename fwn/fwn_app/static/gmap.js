"use strict";

function initMap() {
  const componentForm = [
    'id_street_address',
    'locality',
    'administrative_area_level_1',
    'country',
    'postal_code',
  ];
  const map = new google.maps.Map(document.getElementById("map"), {
    zoom: 11,
    center: {
      lat: 45.5152,
      lng: -122.6784
    },
    mapTypeControl: false,
    fullscreenControl: true,
    zoomControl: true,
    streetViewControl: true
  });
  const marker = new google.maps.Marker({
    map: map,
    draggable: false
  });
  const autocompleteInput = document.getElementById('id_street_address');
  const autocomplete = new google.maps.places.Autocomplete(autocompleteInput, {
    componentRestrictions: { country: ["us", "ca"] },
    fields: ["address_components", "geometry", "name"],
    types: ["address"],
  });
  autocomplete.addListener('place_changed', function() {
    marker.setVisible(false);
    const place = autocomplete.getPlace();
    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert('No details available for input: \'' + place.name + '\'');
      return;
    }
    renderAddress(place);
    fillInAddress(place);
  });

  function fillInAddress(place) { // optional parameter
    const addressNameFormat = {
      'street_number': 'short_name',
      'route': 'long_name',
      'locality': 'long_name',
      'administrative_area_level_1': 'short_name',
      'country': 'long_name',
      'postal_code': 'short_name',
    };
    const getAddressComp = function(type) {
      for (const component of place.address_components) {
        if (component.types[0] === type) {
          return component[addressNameFormat[type]];
        }
      }
      return '';
    };
    document.getElementById('id_street_address').value = getAddressComp('street_number') + ' ' +
      getAddressComp('route');
    document.getElementById('id_city').value = getAddressComp('locality');
    document.getElementById('id_State').value = getAddressComp('administrative_area_level_1');
    document.getElementById('id_zipcode').value = getAddressComp('postal_code');








    // for (const component of componentForm) {
    //   // location field is handled separately above as it has different logic.
    //   if (component !== 'location') {
    //     document.getElementById(component).value = getAddressComp(component);
    //   }
    // }
  }

  function renderAddress(place) {
    map.setCenter(place.geometry.location);
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);
  }
}
