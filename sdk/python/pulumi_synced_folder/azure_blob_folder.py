# coding=utf-8
# *** WARNING: this file was generated by Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['AzureBlobFolderArgs', 'AzureBlobFolder']

@pulumi.input_type
class AzureBlobFolderArgs:
    def __init__(__self__, *,
                 container_name: pulumi.Input[str],
                 path: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 storage_account_name: pulumi.Input[str],
                 disable_managed_object_aliases: Optional[pulumi.Input[bool]] = None,
                 include_hidden_files: Optional[pulumi.Input[bool]] = None,
                 managed_objects: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a AzureBlobFolder resource.
        :param pulumi.Input[str] container_name: The name of the Azure storage container to sync to. Required.
        :param pulumi.Input[str] path: The path (relative or fully-qualified) to the folder containing the files to be synced. Required.
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group that the storage account belongs to. Required.
        :param pulumi.Input[str] storage_account_name: The name of the Azure storage account that the container belongs to. Required.
        :param pulumi.Input[bool] disable_managed_object_aliases: Disables adding an [alias](https://www.pulumi.com/docs/intro/concepts/resources/options/aliases/) resource option to managed objects in the bucket.
        :param pulumi.Input[bool] include_hidden_files: Include hidden files ("dotfiles") when synchronizing folders. Defaults to `false`.
        :param pulumi.Input[bool] managed_objects: Whether to have Pulumi manage files as individual cloud resources. Defaults to `true`.
        """
        pulumi.set(__self__, "container_name", container_name)
        pulumi.set(__self__, "path", path)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "storage_account_name", storage_account_name)
        if disable_managed_object_aliases is not None:
            pulumi.set(__self__, "disable_managed_object_aliases", disable_managed_object_aliases)
        if include_hidden_files is not None:
            pulumi.set(__self__, "include_hidden_files", include_hidden_files)
        if managed_objects is not None:
            pulumi.set(__self__, "managed_objects", managed_objects)

    @property
    @pulumi.getter(name="containerName")
    def container_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure storage container to sync to. Required.
        """
        return pulumi.get(self, "container_name")

    @container_name.setter
    def container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_name", value)

    @property
    @pulumi.getter
    def path(self) -> pulumi.Input[str]:
        """
        The path (relative or fully-qualified) to the folder containing the files to be synced. Required.
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: pulumi.Input[str]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure resource group that the storage account belongs to. Required.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> pulumi.Input[str]:
        """
        The name of the Azure storage account that the container belongs to. Required.
        """
        return pulumi.get(self, "storage_account_name")

    @storage_account_name.setter
    def storage_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_name", value)

    @property
    @pulumi.getter(name="disableManagedObjectAliases")
    def disable_managed_object_aliases(self) -> Optional[pulumi.Input[bool]]:
        """
        Disables adding an [alias](https://www.pulumi.com/docs/intro/concepts/resources/options/aliases/) resource option to managed objects in the bucket.
        """
        return pulumi.get(self, "disable_managed_object_aliases")

    @disable_managed_object_aliases.setter
    def disable_managed_object_aliases(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_managed_object_aliases", value)

    @property
    @pulumi.getter(name="includeHiddenFiles")
    def include_hidden_files(self) -> Optional[pulumi.Input[bool]]:
        """
        Include hidden files ("dotfiles") when synchronizing folders. Defaults to `false`.
        """
        return pulumi.get(self, "include_hidden_files")

    @include_hidden_files.setter
    def include_hidden_files(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_hidden_files", value)

    @property
    @pulumi.getter(name="managedObjects")
    def managed_objects(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to have Pulumi manage files as individual cloud resources. Defaults to `true`.
        """
        return pulumi.get(self, "managed_objects")

    @managed_objects.setter
    def managed_objects(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "managed_objects", value)


class AzureBlobFolder(pulumi.ComponentResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 disable_managed_object_aliases: Optional[pulumi.Input[bool]] = None,
                 include_hidden_files: Optional[pulumi.Input[bool]] = None,
                 managed_objects: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a AzureBlobFolder resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] container_name: The name of the Azure storage container to sync to. Required.
        :param pulumi.Input[bool] disable_managed_object_aliases: Disables adding an [alias](https://www.pulumi.com/docs/intro/concepts/resources/options/aliases/) resource option to managed objects in the bucket.
        :param pulumi.Input[bool] include_hidden_files: Include hidden files ("dotfiles") when synchronizing folders. Defaults to `false`.
        :param pulumi.Input[bool] managed_objects: Whether to have Pulumi manage files as individual cloud resources. Defaults to `true`.
        :param pulumi.Input[str] path: The path (relative or fully-qualified) to the folder containing the files to be synced. Required.
        :param pulumi.Input[str] resource_group_name: The name of the Azure resource group that the storage account belongs to. Required.
        :param pulumi.Input[str] storage_account_name: The name of the Azure storage account that the container belongs to. Required.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AzureBlobFolderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a AzureBlobFolder resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param AzureBlobFolderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AzureBlobFolderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_name: Optional[pulumi.Input[str]] = None,
                 disable_managed_object_aliases: Optional[pulumi.Input[bool]] = None,
                 include_hidden_files: Optional[pulumi.Input[bool]] = None,
                 managed_objects: Optional[pulumi.Input[bool]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 storage_account_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is not None:
            raise ValueError('ComponentResource classes do not support opts.id')
        else:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AzureBlobFolderArgs.__new__(AzureBlobFolderArgs)

            if container_name is None and not opts.urn:
                raise TypeError("Missing required property 'container_name'")
            __props__.__dict__["container_name"] = container_name
            __props__.__dict__["disable_managed_object_aliases"] = disable_managed_object_aliases
            __props__.__dict__["include_hidden_files"] = include_hidden_files
            __props__.__dict__["managed_objects"] = managed_objects
            if path is None and not opts.urn:
                raise TypeError("Missing required property 'path'")
            __props__.__dict__["path"] = path
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if storage_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'storage_account_name'")
            __props__.__dict__["storage_account_name"] = storage_account_name
        super(AzureBlobFolder, __self__).__init__(
            'synced-folder:index:AzureBlobFolder',
            resource_name,
            __props__,
            opts,
            remote=True)

