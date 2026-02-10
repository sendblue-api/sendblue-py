# Changelog

## 1.4.0 (2026-02-10)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/sendblue-api/sendblue-py/compare/v1.3.0...v1.4.0)

### Features

* **api:** manual updates ([50f602d](https://github.com/sendblue-api/sendblue-py/commit/50f602db586f81ba42a02593511b5c2ebfa8e135))
* **client:** add custom JSON encoder for extended type support ([a3dde1a](https://github.com/sendblue-api/sendblue-py/commit/a3dde1a7f956b720455d126e8e283e0897da3356))
* **client:** add support for binary request streaming ([b633405](https://github.com/sendblue-api/sendblue-py/commit/b6334055780560baa92900a4b09e4e94b6e9aad4))


### Bug Fixes

* **docs:** fix mcp installation instructions for remote servers ([53251f5](https://github.com/sendblue-api/sendblue-py/commit/53251f598f9e9d384de13304b5cce74cd9696f56))


### Chores

* bump OpenAPI spec version to 1.1.0 ([7a4f23b](https://github.com/sendblue-api/sendblue-py/commit/7a4f23be6db84ff6f493353f99f40b1c79e13a7f))
* **ci:** upgrade `actions/github-script` ([824940b](https://github.com/sendblue-api/sendblue-py/commit/824940b1e7f05a9960a181190d50a224d543ae71))
* **internal:** bump dependencies ([ce9f013](https://github.com/sendblue-api/sendblue-py/commit/ce9f013adf41d2f8f85e389fa148c5015f92833a))
* **internal:** update `actions/checkout` version ([f6331d0](https://github.com/sendblue-api/sendblue-py/commit/f6331d0c637a9841a4ff4857112f834827c75704))

## 1.3.0 (2026-01-08)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/sendblue-api/sendblue-py/compare/v1.2.0...v1.3.0)

### Features

* **api:** manual updates ([0d0c1eb](https://github.com/sendblue-api/sendblue-py/commit/0d0c1eb6c6421187bdf06c86a5c54b3ce25930aa))


### Bug Fixes

* use async_to_httpx_files in patch method ([e019921](https://github.com/sendblue-api/sendblue-py/commit/e019921b54c8f7aa443b3a7294c7b1c3566f429b))


### Chores

* **internal:** add `--fix` argument to lint script ([89a2517](https://github.com/sendblue-api/sendblue-py/commit/89a2517a8620993fd7761e6a0fe27d66195f5f75))
* **internal:** add missing files argument to base client ([e8f8b46](https://github.com/sendblue-api/sendblue-py/commit/e8f8b46d06435ba29cbf6ea50283f55474c40c4b))
* **internal:** codegen related update ([fb00d54](https://github.com/sendblue-api/sendblue-py/commit/fb00d54033787e43f77c9f30aa524604c9d989ab))
* speedup initial import ([44d1f39](https://github.com/sendblue-api/sendblue-py/commit/44d1f3943f0d5c72c5ef9f923301a8a3b97552d4))


### Documentation

* prominently feature MCP server setup in root SDK readmes ([08e7ce4](https://github.com/sendblue-api/sendblue-py/commit/08e7ce46f1430a3ba68c4506ed3ab31df277f00a))

## 1.2.0 (2025-12-13)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/sendblue-api/sendblue-py/compare/v1.1.0...v1.2.0)

### Features

* **api:** manual updates ([b91ec51](https://github.com/sendblue-api/sendblue-py/commit/b91ec519dfdeccdaae926f15cc3f93c5b89f4ddf))
* **api:** manual updates ([1bf81de](https://github.com/sendblue-api/sendblue-py/commit/1bf81de4f7115baf2c7f89f6116d516b6f3f9e3f))
* **api:** manual updates ([846ef56](https://github.com/sendblue-api/sendblue-py/commit/846ef563e03f81c314178113d2a4adf4053e81e5))
* **api:** manual updates ([32c0d0e](https://github.com/sendblue-api/sendblue-py/commit/32c0d0e2471d621d7953646bfe9bc9e9a1e66764))

## 1.1.0 (2025-12-08)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/sendblue-api/sendblue-py/compare/v1.0.0...v1.1.0)

### Features

* **api/v2/contact:** removed verified field in response example ([e6e1834](https://github.com/sendblue-api/sendblue-py/commit/e6e183450d07d749dfbc0dd00b67c4285a22da62))


### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([4251181](https://github.com/sendblue-api/sendblue-py/commit/4251181fafd406823a552e5ea04e6395dc19c7c9))


### Chores

* **docs:** use environment variables for authentication in code snippets ([15d84c5](https://github.com/sendblue-api/sendblue-py/commit/15d84c56f76ff864ac3744459f82c03f971a422d))
* **internal:** codegen related update ([de6ec9a](https://github.com/sendblue-api/sendblue-py/commit/de6ec9a2eae57d1acfe1f1c790281caede948eb1))
* update lockfile ([39f8a3d](https://github.com/sendblue-api/sendblue-py/commit/39f8a3d403fc62a8b6d80ac14769f9a823f3f9c6))

## 1.0.0 (2025-11-14)

Full Changelog: [v0.0.1...v1.0.0](https://github.com/sendblue-api/sendblue-py/compare/v0.0.1...v1.0.0)

### Features

* **api:** manual updates ([eff2ad8](https://github.com/sendblue-api/sendblue-py/commit/eff2ad812cb31cf31ba5dc0ee45ee3e9d532948f))
* **api:** update via SDK Studio ([7c2d2ed](https://github.com/sendblue-api/sendblue-py/commit/7c2d2edd3a6a5681dc2244b525d92c56d4c05a0b))
* improve future compat with pydantic v3 ([8326eee](https://github.com/sendblue-api/sendblue-py/commit/8326eee9527eb06a2d4a7bcae7ce050888c9858d))
* **types:** replace List[str] with SequenceNotStr in params ([7ce3ef4](https://github.com/sendblue-api/sendblue-py/commit/7ce3ef4b0d80e7c47724b2f34b1267b1c3758d65))


### Bug Fixes

* avoid newer type syntax ([5847fc6](https://github.com/sendblue-api/sendblue-py/commit/5847fc609e1b1092aa382f6c6a64705fd4f12529))


### Chores

* configure new SDK language ([cca5f29](https://github.com/sendblue-api/sendblue-py/commit/cca5f29e389dcb2b24bef4109be3ad799333b5ae))
* do not install brew dependencies in ./scripts/bootstrap by default ([4f7536d](https://github.com/sendblue-api/sendblue-py/commit/4f7536d2eaeda2aab9bb3a1b55a650a98da70130))
* **internal:** add Sequence related utils ([1bcaceb](https://github.com/sendblue-api/sendblue-py/commit/1bcaceb65a87df893a94161c634e68e12cfdcb45))
* **internal:** change ci workflow machines ([1a70fa3](https://github.com/sendblue-api/sendblue-py/commit/1a70fa33929c656589c7d890ee0b756c666ffb46))
* **internal:** detect missing future annotations with ruff ([12703ab](https://github.com/sendblue-api/sendblue-py/commit/12703ab7ae55c3bbfb8f5acdad19f997788372a7))
* **internal:** move mypy configurations to `pyproject.toml` file ([3e558b3](https://github.com/sendblue-api/sendblue-py/commit/3e558b351af2a460387fbbc41f1ba19ba14acee3))
* **internal:** update pydantic dependency ([0be52ab](https://github.com/sendblue-api/sendblue-py/commit/0be52abf84f9494d638ccd667cc64cff3c995789))
* **internal:** update pyright exclude list ([3b5443a](https://github.com/sendblue-api/sendblue-py/commit/3b5443a48bb8f9629d0d6bc31605939fe31de119))
* **tests:** simplify `get_platform` test ([3786de0](https://github.com/sendblue-api/sendblue-py/commit/3786de03d7aedeb692abb0b6907621fd89ad1881))
* **types:** change optional parameter type from NotGiven to Omit ([855077d](https://github.com/sendblue-api/sendblue-py/commit/855077d613cd2ed79d68e20e858b6adb21ef5d11))
* update github action ([989bcab](https://github.com/sendblue-api/sendblue-py/commit/989bcabcf3706cd6b53d0bb5595f608efc1e4fb4))
* update SDK settings ([ae3002f](https://github.com/sendblue-api/sendblue-py/commit/ae3002fdf209414e79d6aaa04144951c403e48c1))
* update SDK settings ([5ab630f](https://github.com/sendblue-api/sendblue-py/commit/5ab630f926f1165e78d17541718c323d86e5ecdb))
* update SDK settings ([ed6498b](https://github.com/sendblue-api/sendblue-py/commit/ed6498b201d6793f14c3b95cbf8f2dcfad83527e))
* update SDK settings ([8118d15](https://github.com/sendblue-api/sendblue-py/commit/8118d15a306c67382f10c5c4ab50fea5e30bda6a))
