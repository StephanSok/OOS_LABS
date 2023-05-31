#include <security/pam_appl.h>
#include <security/pam_misc.h>
#include <stdio.h>

static struct pam_conv conv = {
    misc_conv,
    NULL
};

int main(int argc, char* argv[]) {
    pam_handle_t* authenticator;
    int error_number;

    int return_value;
    const char* user = "nobody";
    
    if (argc == 2) {
        user = argv[1];
    }

    if (argc != 2) {
        fprintf(stderr, "Usage: %s [username]\n", argv[0]);
        return 2;
    }

    return_value = pam_start("check", user, &conv, &authenticator);

    if (return_value == PAM_SUCCESS) {
        return_value = pam_authenticate(authenticator, 0);
        printf("authenticate error code: %s\n", pam_strerror(authenticator, return_value));
    }

    if (return_value == PAM_SUCCESS) {
        return_value = pam_acct_mgmt(authenticator, 0);
        printf("acct_mgmt error code: %s\n", pam_strerror(authenticator, return_value));
    }

    if (return_value == PAM_SUCCESS) {
        printf("Ok auth\n");
    }
     
    if (return_value != PAM_SUCCESS) {
        printf("Bad auth\n");
    }

    if (pam_end(authenticator, return_value) != PAM_SUCCESS) {
        authenticator = NULL;
        fprintf(stderr, "Check user: failed to release authenticator ");
        return 3;
    }

    return (return_value == PAM_SUCCESS ? 0 : 1);
}
