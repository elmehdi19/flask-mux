from flask import request
from flask_mux import Router
from testing.common import is_auth, is_admin, is_json, mock_middleware

test_mws_router = Router(__name__)


def get_basic():
    return {"success": True}


def get_with_auth():
    return {"success": True, "admin": request.headers.get("admin")}


def get_with_multi_mws():
    return {"success": True, "admin": request.headers.get("admin")}


def get_with_extra_mws():
    return {"success": True, "admin": request.headers.get("admin")}


test_mws_router.get("/basic", get_basic)
test_mws_router.get("/get-with-auth", is_admin, get_with_auth)
test_mws_router.get("/get-with-multi-mws", is_auth,
                    is_admin, get_with_multi_mws)
test_mws_router.get(
    "/get-with-extra-mws",
    mock_middleware,
    mock_middleware,
    mock_middleware,
    is_auth,
    is_admin,
    get_with_extra_mws,
)


def post_basic():
    return {"success": True}


def post_with_one_mw():
    return {"success": True, "req_body": request.json}


def post_with_multi_mws():
    return {"success": True, "req_body": request.json}


def post_with_extra_mws():
    return {
        "success": True,
        "req_body": request.json,
        "admin": request.headers.get("admin"),
    }


test_mws_router.post("/basic", post_basic)
test_mws_router.post("/one-mw", is_json, post_with_one_mw)
test_mws_router.post("/multi-mws", is_auth, is_json, post_with_multi_mws)
test_mws_router.post(
    "/extra-mws",
    mock_middleware,
    mock_middleware,
    mock_middleware,
    mock_middleware,
    is_auth,
    is_admin,
    is_json,
    post_with_extra_mws,
)


def handle_basic():
    return {"success": True, "method": request.method}


def handle_with_one_mw():
    return {"success": True, "method": request.method}


def handle_with_multi_mws():
    return {"success": True, "req_body": request.json, "method": request.method}


def handle_with_extra_mws():
    return {
        "success": True,
        "req_body": request.json,
        "admin": request.headers.get("admin"),
        "method": request.method,
    }


test_mws_router.handle("/handle-basic", handle_basic)
test_mws_router.handle("/handle-one-mw", is_auth, handle_with_one_mw)
test_mws_router.handle("/handle-multi-mws", is_auth,
                       is_json, handle_with_multi_mws)

test_mws_router.handle(
    "/handle-extra-mws",
    mock_middleware,
    mock_middleware,
    mock_middleware,
    mock_middleware,
    is_auth,
    is_admin,
    is_json,
    handle_with_extra_mws,
)


def put_basic():
    return {"success": True}


def put_with_one_mw():
    return {"success": True, "req_body": request.json}


def put_with_multi_mws():
    return {"success": True, "req_body": request.json}


def put_with_extra_mws():
    return {
        "success": True,
        "req_body": request.json,
        "admin": request.headers.get("admin"),
    }


test_mws_router.put("/basic", put_basic)
test_mws_router.put("/one-mw", is_json, put_with_one_mw)
test_mws_router.put("/multi-mws", is_auth, is_json, put_with_multi_mws)
test_mws_router.put(
    "/extra-mws",
    mock_middleware,
    mock_middleware,
    mock_middleware,
    mock_middleware,
    is_auth,
    is_admin,
    is_json,
    put_with_extra_mws,
)


def delete_basic():
    return {"success": True}


def delete_with_one_mw():
    return {"success": True, "req_body": request.json}


def delete_with_multi_mws():
    return {"success": True, "req_body": request.json}


def delete_with_extra_mws():
    return {
        "success": True,
        "req_body": request.json,
        "admin": request.headers.get("admin"),
    }


test_mws_router.delete("/basic", delete_basic)
test_mws_router.delete("/one-mw", is_json, delete_with_one_mw)
test_mws_router.delete("/multi-mws", is_auth, is_json, delete_with_multi_mws)
test_mws_router.delete(
    "/extra-mws",
    mock_middleware,
    mock_middleware,
    mock_middleware,
    mock_middleware,
    is_auth,
    is_admin,
    is_json,
    delete_with_extra_mws,
)


def patch_basic():
    return {"success": True}


def patch_with_one_mw():
    return {"success": True, "req_body": request.json}


def patch_with_multi_mws():
    return {"success": True, "req_body": request.json}


def patch_with_extra_mws():
    return {
        "success": True,
        "req_body": request.json,
        "admin": request.headers.get("admin"),
    }


test_mws_router.patch("/basic", patch_basic)
test_mws_router.patch("/one-mw", is_json, patch_with_one_mw)
test_mws_router.patch("/multi-mws", is_auth, is_json, patch_with_multi_mws)
test_mws_router.patch(
    "/extra-mws",
    mock_middleware,
    mock_middleware,
    mock_middleware,
    mock_middleware,
    is_auth,
    is_admin,
    is_json,
    patch_with_extra_mws,
)
