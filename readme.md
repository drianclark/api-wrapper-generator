# API Wrapper Generator

## Basic Principle
The wrapper generator generates basic Python API wrappers for any API given its OpenAPI spec. 

It is comprised of four component classes:
1. WrapperGenerator
1. EndpointFunctionsGenerator
1. ClassesGenerator
1. TestsGenerator

The WrapperGenerator class combines the functionality of the EndpointFunction and ClassesGenerator classes. It is also where the CLI resides and should be the main point of entry if the generator is treated as a stand-alone program.

### WrapperGenerator

- contains the CLI
- generates the config file
- makes use of the EndpointFunctionsGenerator and ClassesGenerator classes to generate a wrapper

### EndpointFunctionsGenerator

- uses the requests package to generate functions that consume each endpoint in the API
- each function returns a Python object / list of objects that correspond to a component in the spec

### ClassesGenerator
- generates a corresponding Python class for each component in the spec

### TestsGenerator
- generates tests for the generated wrapper
- tests endpoint functions and their return values (both existence of properties and their types)

## Limitations
- The need for config. The CLI was created to make config generation more user friendly, but eradicating the need for it is ideal. This can potentially be solved by adding extension fields to the spec, as discussed with Mihajlo.
- I only had time to look at the hydrology API spec, so there are bound to be some incorrect assumptions about the general format of API specs which could cause errors
- No tests are generated for endpoints with params embedded within the url. For example, '/id/measures/{id}'- how do we know what this id should be?
- In testing, handling nested property errors that are dependent on the ancestor properties is limited. The error is handled correctly only for the parent, but not for "higher"(?) ancestors. For example a property could be specified as non-nullable, but its parent could be nullable. The test could then fail because if the parent property is null, an error would be thrown trying to access the child property. This is handled, fixed, and re-tested by the current program, but if the "grandparent" property is null, the test just states what it thinks the problem is without retesting under the correct conditions. 
- In testing, some properties in the spec could be mislabelled as having type object when they are arrays. This is handled similarly to the one above: works up to the parent property, but no higher
- The ClassesGenerator only uses the default views, so the generated classes could be missing fields only found in other views.


## Next Steps
- Refactoring, especially the testGenerator class
- Cleaning up Jinja template
- Have to maintain a rename map available to all classes to avoid errors when renaming an auto-detected base class (not a problem once the configuration becomes entirely automated and renaming base classes is no longer necessary)
