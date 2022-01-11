// Braintee payment form creation and intregration
var form = document.querySelector('#checkout-form');
var submit = document.querySelector('#checkout-submit');
// retrieving client_token from template
const client_token = JSON.parse(document.getElementById('client_token').textContent);

// Braintree client token
braintree.client.create({
    authorization: client_token
}, function (clientErr, clientInstance) {
    if (clientErr) {
        return;
    }

    // Braintree hosted fields
    braintree.hostedFields.create({
        client: clientInstance,
        styles: {
            'input': {
                'font-size': '1rem',
                'border-color': 'black',
            },
            'input.invalid': {
                'color': 'red'
            },
            'input.valid': {
                'color': 'green'
            }
        },
        fields: {
            number: {
                container: '#card-number',
                placeholder: 'card number ex. 4111 •••• •••• ••11',
            },
            cvv: {
                container: '#cvv',
                placeholder: 'cvv ex. 123',
            },
            expirationDate: {
                container: '#expiration-date',
                placeholder: 'exp. date ex. 10/2022'
            }
        }
    }, function (hostedFieldsErr, hostedFieldsInstance) {
        if (hostedFieldsErr) {
            return;
        }
        // Braintree validation for hosted fields from
        // https://codepen.io/braintree/pen/zeamxM
 
        function createInputChangeEventListener(element) {
            return function () {
                validateInput(element);
            };
        }

        function setValidityClasses(element, validity) {
            if (validity) {
                element.removeClass('is-invalid');
                element.addClass('is-valid');
            } else {
                element.addClass('is-invalid');
                element.removeClass('is-valid');
            }
        }

        function validateInput(element) {
            // validation - if fields are empty, mark them
            // as invalid, if not, mark them as valid
            if (!element.val().trim()) {
                setValidityClasses(element, false);
                return false;
            }
            setValidityClasses(element, true);
            return true;
        }

        hostedFieldsInstance.on('validityChange', function (event) {
            var field = event.fields[event.emittedBy];

            // Remove any previously applied error or warning classes
            $(field.container).removeClass('is-valid');
            $(field.container).removeClass('is-invalid');

            if (field.isValid) {
                $(field.container).addClass('is-valid');
            } else if (field.isPotentiallyValid) {
                // skip adding classes if the field is
                // not valid, but is potentially valid
            } else {
                $(field.container).addClass('is-invalid');
            }
        });

        // Form submission
        submit.removeAttribute('disabled');
        form.addEventListener('submit', function (event) {
            event.preventDefault();
            var formIsInvalid = false;
            var state = hostedFieldsInstance.getState();
            // Loop through the Hosted Fields and check
            // for validity, apply the is-invalid class
            // to the field container if invalid
            Object.keys(state.fields).forEach(function (field) {
                if (!state.fields[field].isValid) {
                    $(state.fields[field].container).addClass('is-invalid');
                    formIsInvalid = true;
                }
            });

            if (formIsInvalid) {
                // skip tokenization request if any fields are invalid
                return;
            }

            hostedFieldsInstance.tokenize(function (tokenizeErr, payload) {
                if (tokenizeErr) {
                    return;
                }
                // Paiement submission
                document.querySelector('input[name="payment_method_nonce"]').value = payload.nonce;
                document.getElementById('checkout-form').submit();
            });
        }, false);
    });

});