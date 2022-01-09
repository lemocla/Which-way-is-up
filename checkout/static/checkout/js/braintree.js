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
        console.error(clientErr);
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
                placeholder: 'card number ex. 4111 1111 1111 1111',
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
            console.error(hostedFieldsErr);
            return;
        }

        submit.removeAttribute('disabled');

        form.addEventListener('submit', function (event) {
            event.preventDefault();

            hostedFieldsInstance.tokenize(function (tokenizeErr, payload) {
                if (tokenizeErr) {
                    console.error(tokenizeErr);
                    return;
                }
                // Paiement submission
                document.querySelector('input[name="payment_method_nonce"]').value = payload.nonce;
                document.getElementById('checkout-form').submit();
            });
        }, false);
    });

});