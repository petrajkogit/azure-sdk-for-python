# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class ActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the action.
    """

    EMAIL_CONTACTS = "EmailContacts"
    AUTO_RENEW = "AutoRenew"

class DeletionRecoveryLevel(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Reflects the deletion recovery level currently in effect for keys in the current vault. If it
    contains 'Purgeable' the key can be permanently deleted by a privileged user; otherwise, only
    the system can purge the key, at the end of the retention interval.
    """

    PURGEABLE = "Purgeable"  #: Soft-delete is not enabled for this vault. A DELETE operation results in immediate and irreversible data loss.
    RECOVERABLE_PURGEABLE = "Recoverable+Purgeable"  #: Soft-delete is enabled for this vault; A privileged user may trigger an immediate, irreversible deletion(purge) of a deleted entity.
    RECOVERABLE = "Recoverable"  #: Soft-delete is enabled for this vault and purge has been disabled. A deleted entity will remain in this state until recovered, or the end of the retention interval.
    RECOVERABLE_PROTECTED_SUBSCRIPTION = "Recoverable+ProtectedSubscription"  #: Soft-delete is enabled for this vault, and the subscription is protected against immediate deletion.

class JsonWebKeyCurveName(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Elliptic curve name. For valid values, see JsonWebKeyCurveName.
    """

    P256 = "P-256"  #: The NIST P-256 elliptic curve, AKA SECG curve SECP256R1.
    P384 = "P-384"  #: The NIST P-384 elliptic curve, AKA SECG curve SECP384R1.
    P521 = "P-521"  #: The NIST P-521 elliptic curve, AKA SECG curve SECP521R1.
    SECP256_K1 = "SECP256K1"  #: The SECG SECP256K1 elliptic curve.

class JsonWebKeyEncryptionAlgorithm(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """algorithm identifier
    """

    RSA_OAEP = "RSA-OAEP"
    RSA_OAEP256 = "RSA-OAEP-256"
    RSA1_5 = "RSA1_5"

class JsonWebKeyOperation(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """JSON web key operations. For more information, see JsonWebKeyOperation.
    """

    ENCRYPT = "encrypt"
    DECRYPT = "decrypt"
    SIGN = "sign"
    VERIFY = "verify"
    WRAP_KEY = "wrapKey"
    UNWRAP_KEY = "unwrapKey"

class JsonWebKeySignatureAlgorithm(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The signing/verification algorithm identifier. For more information on possible algorithm
    types, see JsonWebKeySignatureAlgorithm.
    """

    PS256 = "PS256"
    PS384 = "PS384"
    PS512 = "PS512"
    RS256 = "RS256"
    RS384 = "RS384"
    RS512 = "RS512"
    RSNULL = "RSNULL"
    ES256 = "ES256"
    ES384 = "ES384"
    ES512 = "ES512"
    ECDSA256 = "ECDSA256"

class JsonWebKeyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """JsonWebKey key type (kty).
    """

    EC = "EC"
    EC_HSM = "EC-HSM"
    RSA = "RSA"
    RSA_HSM = "RSA-HSM"
    OCT = "oct"

class KeyUsageType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    DIGITAL_SIGNATURE = "digitalSignature"
    NON_REPUDIATION = "nonRepudiation"
    KEY_ENCIPHERMENT = "keyEncipherment"
    DATA_ENCIPHERMENT = "dataEncipherment"
    KEY_AGREEMENT = "keyAgreement"
    KEY_CERT_SIGN = "keyCertSign"
    C_RL_SIGN = "cRLSign"
    ENCIPHER_ONLY = "encipherOnly"
    DECIPHER_ONLY = "decipherOnly"
